<script>
    import { Field, ErrorMessage } from "sveltik";

    export let label
    export let name
    export let type = "text"

    let errorClasses = "pr-10 border-red-300 text-red-900 placeholder-red-300"
</script>

<Field {name} let:field let:meta>
<div>
    <label for={name} class="block text-sm font-medium text-gray-700">{label}</label>
    <div class="mt-1 relative rounded-md shadow-sm">
        <input id={name}
               {type}
               {...field}
               on:input={field.handleInput}
               on:blur={field.handleBlur}
               on:keydown
               {...$$restProps}
               class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-yellow-400 focus:border-yellow-400 sm:text-sm {(meta.touched && meta.error) && errorClasses}">
        {#if meta.touched && meta.error}
            <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                <svg class="h-5 w-5 text-red-500" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                    <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                </svg>
            </div>
        {/if}
    </div>
    <ErrorMessage {name} as="p" class="mt-2 text-sm text-red-600" />
</div>
</Field>

