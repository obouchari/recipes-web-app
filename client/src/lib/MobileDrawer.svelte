<script>
    import Transition from 'svelte-class-transition';

    import logo from "./Header/spicety-logo.svg"

    export let isOpen = false;

    function toggleDrawer() {
        isOpen = !isOpen;
    }

</script>

<Transition
        toggle={isOpen}
        transitions="transition"
        inTransition="ease-in-out duration-300"
        outTransition="ease-in-out duration-300"
        inState="opacity-90"
        onState="opacity-100"
        outState="opacity-90"
>
<div class="fixed inset-0 overflow-hidden z-10" aria-labelledby="slide-over-title" role="dialog" aria-modal="true">
    <div class="absolute inset-0 overflow-hidden">

        <Transition
                toggle={isOpen}
                transitions="transition"
                inTransition="ease-in-out duration-300"
                outTransition="ease-in-out duration-300"
                inState="opacity-0"
                onState="opacity-100"
                outState="opacity-0"
        >
        <div class="absolute inset-0 bg-gray-500 bg-opacity-75 transition-opacity"
             aria-hidden="true"></div>
        </Transition>

        <div class="fixed inset-y-0 left-0 pr-20 max-w-full flex">
            <Transition
                    toggle={isOpen}
                    transitions="transition transform"
                    inTransition="ease-in-out duration-300"
                    outTransition="ease-in-out duration-300"
                    inState="-translate-x-full"
                    onState="translate-x-0"
                    outState="-translate-x-full"
            >
                <div class="w-screen max-w-sm">
                    <div class="h-full flex flex-col py-6 bg-gray-100 shadow-xl overflow-y-scroll">
                        <div class="px-4 sm:px-6">
                            <div class="flex items-start justify-between">
                                <div class="flex-shrink-0">
                                    <img class="block h-8 w-8"
                                         src={logo} alt="Spicety">
                                </div>
                                <div class="ml-3 h-7 flex items-center">
                                    <button type="button"
                                            on:click={toggleDrawer}
                                            class="rounded-md text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500">
                                        <span class="sr-only">Close panel</span>
                                        <!-- Heroicon name: outline/x -->
                                        <svg class="h-8 w-8" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                                        </svg>
                                    </button>
                                </div>
                            </div>
                        </div>
                        <div class="mt-6 relative flex-1 px-4 sm:px-6">
                            <slot/>
                        </div>
                    </div>
                </div>
            </Transition>
        </div>

    </div>
</div>
</Transition>