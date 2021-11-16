<script>
    import Transition from 'svelte-class-transition'
    import InputField from "$lib/forms/InputField.svelte"

    let isOpen = false
    let isLoading = false
    let value

    export let label
    export let name
    export let items = []
    export let onEnter = (e) => {}

    function toggleDropdown() {
        isOpen = !isOpen
    }

    function handleKeyUp(e) {
        if (e.code === "Enter") {
            console.log("fetch api")
        } else if (e.keyCode >= 65 && e.keyCode <= 90) {
            setTimeout(() => {
                if (value.length > 1) {
                    isLoading = true
                    isOpen = true
                }
            }, 500)
        }
    }

    function handleChange(e) {
        if (!value.length)
            isOpen = false
    }

    function handleFocus() {
        if (value.length)
            isOpen = true
    }

    function handleBlue() {
        isOpen = false
    }
</script>



<div class="relative inline-block text-left w-full">
    <label for={name} class="block text-sm font-medium text-gray-700">{label}</label>
    <input id={name}
           type="text"
           bind:value
           on:keyup|trusted={handleKeyUp}
           on:input|trusted={handleChange}
           on:focus={handleFocus}
           on:blur={handleBlue}
           autocomplete="off"
           {...$$restProps}
           class="appearance-none block mt-1 w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-yellow-400 focus:border-yellow-400 sm:text-sm">

    <Transition
            toggle={isOpen}
            transitions="transition transform"
            inTransition="ease-out duration-100"
            outTransition="ease-in duration-75"
            inState="opacity-0 scale-95"
            onState="opacity-100 scale-100"
            outState="opacity-0 scale-95"
    >
    <div class="origin-top-right absolute right-0 mt-2 w-full rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 focus:outline-none" role="menu" aria-orientation="vertical" aria-labelledby="menu-button" tabindex="-1">
        <div class="py-1" role="none">
            {#if isLoading}
            <p class="text-gray-700 block px-4 py-2 text-sm">Loading data...</p>
            {:else}
            <!-- Active: "bg-gray-100 text-gray-900", Not Active: "text-gray-700" -->
            <a href="#" class="text-gray-700 block px-4 py-2 text-sm" role="menuitem" tabindex="-1" id="menu-item-0">Account settings</a>
            <a href="#" class="text-gray-700 block px-4 py-2 text-sm" role="menuitem" tabindex="-1" id="menu-item-1">Support</a>
            <a href="#" class="text-gray-700 block px-4 py-2 text-sm" role="menuitem" tabindex="-1" id="menu-item-2">License</a>
            {/if}
        </div>
    </div>
    </Transition>
</div>