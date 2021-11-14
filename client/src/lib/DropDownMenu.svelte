<script>
    import Transition from 'svelte-class-transition';

    let isOpen = false;

    function clickOutside(node, {enabled: initialEnabled, cb}) {
        const handleOutsideClick = ({target}) => {
            if (!node.contains(target)) {
                cb();
            }
        };

        function update({enabled}) {
            if (enabled) {
                window.addEventListener('click', handleOutsideClick);
            } else {
                window.removeEventListener('click', handleOutsideClick);
            }
        }

        update(initialEnabled);
        return {
            update,
            destroy() {
                window.removeEventListener('click', handleOutsideClick);
            }
        };
    }

    function toggleDropdown() {
        isOpen = !isOpen;
    }

    export let divide = false
    let divideClasses = "divide-y divide-gray-100"

</script>


<div class="ml-3 relative flex-shrink-0" use:clickOutside={{ enabled: isOpen, cb: () => (isOpen = false) }}>
    <div>
        <button type="button"
                class="bg-yellow-400 rounded-full flex text-sm text-white focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-yellow-400 focus:ring-white"
                id="user-menu-button" aria-expanded="false" aria-haspopup="true" on:click={toggleDropdown}>
            <span class="sr-only">Open user menu</span>
            <img class="rounded-full h-8 w-8"
                 src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
                 alt="">
        </button>
    </div>


    <Transition
            toggle={isOpen}
            transitions="transition transform"
            inTransition="ease-out duration-100"
            outTransition="ease-in duration-75"
            inState="opacity-0 scale-95"
            onState="opacity-100 scale-100"
            outState="opacity-0 scale-95"
    >
        <div class="origin-top-right z-10 absolute right-0 mt-2 w-48 rounded-md shadow-lg py-1 bg-white ring-1 ring-black ring-opacity-5 focus:outline-none {divide && divideClasses}"
             role="menu" aria-orientation="vertical" aria-labelledby="user-menu-button"
             tabindex="-1">
            <slot/>
        </div>
    </Transition>
</div>