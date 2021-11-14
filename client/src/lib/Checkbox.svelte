<script>
    import { Field } from "sveltik";

    export let label
    export let name
</script>

<Field {name} let:field let:meta>
    <div class="flex items-center">
        <input id={name}
               {name}
               {...field}
               on:input={field.handleInput}
               on:blur={field.handleBlur}
               type="checkbox"
               class="h-4 w-4 text-red-600 focus:ring-red-500 border-gray-300 rounded">
        <label for={name} class="ml-2 block text-sm text-gray-900">
            {label}
        </label>
    </div>
</Field>

