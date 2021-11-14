<script>
    import Transition from 'svelte-class-transition';

    // Import icons
    import mainDishIcon from "./icons/main-dish.svg"
    import sideDishIcon from "./icons/side-dish.svg"
    import appetizerIcon from "./icons/appetizer.svg"
    import dessertIcon from "./icons/dessert.svg"
    import beverageIcon from "./icons/beverage.svg"
    import snackIcon from "./icons/snack.svg"

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
</script>

<div class="relative" use:clickOutside={{ enabled: isOpen, cb: () => (isOpen = false) }}>
    <!-- Item active: "text-gray-900", Item inactive: "text-gray-500" -->
    <button type="button"
            class="group rounded-md py-2 px-3 inline-flex items-center text-sm font-medium text-gray-800 hover:bg-yellow-500 hover:bg-opacity-75 focus:outline-none focus:ring-2 focus:ring-yellow-100"
            aria-expanded="false"
            on:click={toggleDropdown}>
        <span>By Categories</span>
        <svg class="text-gray-800 ml-2 h-5 w-5 transition ease-in-out duration-150" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
            <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" />
        </svg>
    </button>

    <Transition
            toggle={isOpen}
            transitions="transition"
            inTransition="ease-out duration-200"
            outTransition="ease-in duration-150"
            inState="opacity-0 translate-y-1"
            onState="opacity-100 translate-y-0"
            outState="opacity-0 translate-y-1"
    >
    <div class="absolute z-10 -left-1/2 mt-2 px-2 w-screen max-w-md sm:px-0 lg:max-w-3xl">
        <div class="rounded-lg shadow-lg ring-1 ring-black ring-opacity-5 overflow-hidden">
            <div class="relative grid gap-6 bg-white px-5 py-6 sm:gap-8 sm:p-8 lg:grid-cols-2">
                <a href="#" class="-m-3 p-3 flex items-start rounded-lg hover:bg-gray-50 transition ease-in-out duration-150">
                    <div class="flex-shrink-0 flex items-center justify-center h-10 w-10 rounded-md bg-yellow-400 text-gray-700 sm:h-12 sm:w-12">
                        <img class="block h-8 w-8" src={mainDishIcon} alt="Main Dish">
                    </div>
                    <div class="ml-4">
                        <p class="text-base font-medium text-gray-900">
                            Main Dishes
                        </p>
                        <p class="mt-1 text-sm text-gray-500">
                            Get a better understanding of where your traffic is coming from.
                        </p>
                    </div>
                </a>

                <a href="#" class="-m-3 p-3 flex items-start rounded-lg hover:bg-gray-50 transition ease-in-out duration-150">
                    <div class="flex-shrink-0 flex items-center justify-center h-10 w-10 rounded-md bg-yellow-400 text-gray-700 sm:h-12 sm:w-12">
                        <img class="block h-8 w-8" src={sideDishIcon} alt="Main Dish">
                    </div>
                    <div class="ml-4">
                        <p class="text-base font-medium text-gray-900">
                            Side Dishes
                        </p>
                        <p class="mt-1 text-sm text-gray-500">
                            Speak directly to your customers in a more meaningful way.
                        </p>
                    </div>
                </a>

                <a href="#" class="-m-3 p-3 flex items-start rounded-lg hover:bg-gray-50 transition ease-in-out duration-150">
                    <div class="flex-shrink-0 flex items-center justify-center h-10 w-10 rounded-md bg-yellow-400 text-gray-700 sm:h-12 sm:w-12">
                        <img class="block h-8 w-8" src={appetizerIcon} alt="Main Dish">
                    </div>
                    <div class="ml-4">
                        <p class="text-base font-medium text-gray-900">
                            Appetizers
                        </p>
                        <p class="mt-1 text-sm text-gray-500">
                            Your customers&#039; data will be safe and secure.
                        </p>
                    </div>
                </a>

                <a href="#" class="-m-3 p-3 flex items-start rounded-lg hover:bg-gray-50 transition ease-in-out duration-150">
                    <div class="flex-shrink-0 flex items-center justify-center h-10 w-10 rounded-md bg-yellow-400 text-gray-700 sm:h-12 sm:w-12">
                        <img class="block h-8 w-8" src={dessertIcon} alt="Main Dish">
                    </div>
                    <div class="ml-4">
                        <p class="text-base font-medium text-gray-900">
                            Desserts
                        </p>
                        <p class="mt-1 text-sm text-gray-500">
                            Connect with third-party tools that you&#039;re already using.
                        </p>
                    </div>
                </a>

                <a href="#" class="-m-3 p-3 flex items-start rounded-lg hover:bg-gray-50 transition ease-in-out duration-150">
                    <div class="flex-shrink-0 flex items-center justify-center h-10 w-10 rounded-md bg-yellow-400 text-gray-700 sm:h-12 sm:w-12">
                        <img class="block h-8 w-8" src={beverageIcon} alt="Main Dish">
                    </div>
                    <div class="ml-4">
                        <p class="text-base font-medium text-gray-900">
                            Beverages
                        </p>
                        <p class="mt-1 text-sm text-gray-500">
                            Build strategic funnels that will drive your customers to convert
                        </p>
                    </div>
                </a>

                <a href="#" class="-m-3 p-3 flex items-start rounded-lg hover:bg-gray-50 transition ease-in-out duration-150">
                    <div class="flex-shrink-0 flex items-center justify-center h-10 w-10 rounded-md bg-yellow-400 text-gray-700 sm:h-12 sm:w-12">
                        <img class="block h-8 w-8" src={snackIcon} alt="Main Dish">
                    </div>
                    <div class="ml-4">
                        <p class="text-base font-medium text-gray-900">
                            Snacks
                        </p>
                        <p class="mt-1 text-sm text-gray-500">
                            Get detailed reports that will help you make more informed decisions
                        </p>
                    </div>
                </a>
            </div>
        </div>
    </div>
    </Transition>
</div>
