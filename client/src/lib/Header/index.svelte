<script>
    import { url } from "@roxi/routify";

    import logo from "./spicety-logo.svg"
    import DropDownMenu from "$lib/DropDownMenu/index.svelte"
    import DropDownMenuItem from "$lib/DropDownMenu/MenuItem.svelte"
    import NavItem from "$lib/Header/NavItem.svelte"
    import { user } from "$stores/user"
    import MobileDrawer from "$lib/MobileDrawer.svelte";
    import SignOutButton from "$lib/forms/SignOutButton.svelte";
    import MobileNavItem from "$lib/Header/MobileNavItem.svelte";
    import CategoryMenu from "$lib/Header/CategoryMenu/index.svelte";

    let isLoggedIn
    let email
    let fullName

    user.subscribe(user => {
        isLoggedIn = user.isLoggedIn
        email = user.email
        fullName = `${user.first_name} ${user.last_name}`
    })

    let mainNavLinks = [
        ["/index", "Home"],
    ]

    let profileNavLinks = [
        ["/auth/profile", "Your Profile"],
        ["/auth/recipes", "Your Recipes"],
        ["/auth/bookmarks", "Your Bookmarks"],
        ["/auth/settings", "Account Settings"],
    ]

    let drawerVisible = false

    function toggleDrawer() {
        drawerVisible = !drawerVisible
    }
</script>

<div class="bg-yellow-400 pb-32">
    <nav class="bg-yellow-400 border-b border-yellow-600 border-opacity-25 lg:border-none">
        <div class="max-w-7xl mx-auto px-2 sm:px-4 lg:px-8">
            <div class="relative h-16 flex items-center justify-between lg:border-b lg:border-yellow-600 lg:border-opacity-25">
                <div class="px-2 flex items-center lg:px-0">
                    <div class="flex-shrink-0">
                        <img class="block h-8 w-8"
                             src={logo} alt="Spicety">
                    </div>
                    <div class="hidden lg:block lg:ml-10">
                        <div class="flex space-x-4">
                            {#each mainNavLinks as [path, name]}
                                <NavItem {name} {path} />
                            {/each}
                            <CategoryMenu/>
                            {#if isLoggedIn}
                            <NavItem name="Create Recipe" path="/auth/create-recipe" />
                            {/if}
                        </div>
                    </div>
                </div>
                <div class="flex-1 px-2 flex justify-center lg:ml-6 lg:justify-end">
                    <div class="max-w-lg w-full lg:max-w-sm">
                        <label for="search" class="sr-only">Search recipes</label>
                        <div class="relative text-gray-400 focus-within:text-gray-600">
                            <div class="pointer-events-none absolute inset-y-0 left-0 pl-3 flex items-center">
                                <!-- Heroicon name: solid/search -->
                                <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"
                                     fill="currentColor" aria-hidden="true">
                                    <path fill-rule="evenodd"
                                          d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
                                          clip-rule="evenodd"/>
                                </svg>
                            </div>
                            <input id="search"
                                   class="block w-full bg-gray-50 py-2 pl-10 pr-3 border border-transparent rounded-md leading-5 text-gray-900 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-yellow-400 focus:ring-white focus:border-white sm:text-sm"
                                   placeholder="Look for recipes..." type="search" name="search">
                        </div>
                    </div>
                </div>
                <div class="flex lg:hidden">
                    <!-- Mobile menu button -->
                    <button type="button"
                            class="rounded-md inline-flex items-center justify-center text-gray-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-800 focus:ring-yellow-300"
                            aria-controls="mobile-menu"
                            aria-expanded="false"
                            on:click={toggleDrawer}>
                        <span class="sr-only">Open main menu</span>
                        <!-- Heroicon name: outline/menu -->
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
                        </svg>
                    </button>
                </div>
                <div class="hidden lg:block lg:ml-4">
                    <div class="flex items-center">
                        {#if isLoggedIn}
                        <!-- Profile dropdown -->
                            <DropDownMenu divide>
                                <div class="px-4 py-3" role="none">
                                    <p class="text-sm" role="none">
                                        Signed in as
                                    </p>
                                    <p class="text-sm font-medium text-gray-900 truncate" role="none">
                                        {email}
                                    </p>
                                </div>
                                <div class="py-1" role="none">
                                    {#each profileNavLinks as [path, name]}
                                        <DropDownMenuItem {name} {path}/>
                                    {/each}
                                </div>
                                <div class="py-3 px-3" role="none">
                                    <SignOutButton/>
                                </div>
                            </DropDownMenu>
                        {:else}
                            <a href={$url("/login")}
                               sveltekit:prefetch
                               class="inline-flex items-center px-4 py-2 border-2 border-red-500 text-sm font-medium rounded-md text-red-500 hover:bg-red-500 hover:text-white focus:outline-none focus:ring-2 focus:ring-yellow-100">
                                Sign in
                            </a>
                            <a href={$url("/signup")}
                               sveltekit:prefetch
                               class="ml-2 inline-flex items-center px-4 py-2 border-2 border-transparent text-sm font-medium rounded-md text-white bg-red-500 focus:outline-none focus:ring-2 focus:ring-yellow-100">
                                Sign up
                            </a>
                        {/if}
                    </div>
                </div>
            </div>
        </div>

        <!-- Mobile menu, show/hide based on menu state. -->
        <MobileDrawer bind:isOpen={drawerVisible} >
            <div class="lg:hidden" id="mobile-menu">
                <div class="-mx-4 pt-4 pb-3 divide-y divide-gray-300">
                    {#if isLoggedIn}
                        <div class="px-6 mb-8 flex items-center">
                            <div class="flex-shrink-0">
                                <img class="rounded-full h-12 w-12"
                                     src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
                                     alt="">
                            </div>
                            <div class="ml-3">
                                <div class="text-base font-medium text-gray-800">{fullName}</div>
                                <div class="text-sm font-medium text-gray-400">{email}</div>
                            </div>
                        </div>
                        <div class="py-8 space-y-1">
                            {#each profileNavLinks as [path, name]}
                                <MobileNavItem {name} {path} onClick={toggleDrawer} />
                            {/each}
                        </div>
                    {/if}
                    <div class="py-8 space-y-1">
                        {#each mainNavLinks as [path, name]}
                            <MobileNavItem {name} {path} onClick={toggleDrawer} />
                        {/each}
                    </div>
                    {#if isLoggedIn}
                        <div class="px-6 py-8 space-y-1">
                            <SignOutButton/>
                        </div>
                    {:else}
                        <div class="px-6 py-8 space-y-3">
                            <a href={$url("/signup")}
                               on:click={toggleDrawer}
                               class="block rounded-md py-2 px-3 text-center text-base font-medium bg-red-500 text-white hover:bg-opacity-75">
                                Sign up
                            </a>
                            <a href={$url("/login")}
                               on:click={toggleDrawer}
                               class="block rounded-md border-2 border-red-500 py-2 px-3 text-center text-base font-medium text-red-500 hover:bg-opacity-75">
                                Sign in
                            </a>
                        </div>
                    {/if}
                </div>
            </div>
        </MobileDrawer>
    </nav>
    <header class="py-10">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <h1 class="text-2xl text-gray-800">
                Welcome to <span class="text-3xl font-bold">Spicety!</span><br/>
                <span class="text-xl">Find the best recipes for all food enthusiasts.</span>
            </h1>
        </div>
    </header>
</div>

