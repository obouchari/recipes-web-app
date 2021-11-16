<script>
    import {url} from "@roxi/routify";

    import { user } from "$stores/user"
    import addRecipeIcon from "./add-recipe.svg"

    let isLoggedIn

    user.subscribe(user => {
        isLoggedIn = user.isLoggedIn
    })

    export let title = "No Recipes"
</script>


<div class="text-center w-full flex flex-col justify-center py-6">
    <img class="mx-auto h-16 w-16" src={addRecipeIcon} alt="Create Recipe Icon">
    <h3 class="mt-2 text-sm font-medium text-gray-900">{title}</h3>
    <p class="mt-1 text-sm text-gray-500">
        {#if isLoggedIn}
            Get started by adding a new recipe.
        {:else}
            Login to add a new recipe
        {/if}
    </p>
    {#if isLoggedIn}
    <div class="mt-6">
        <a href={$url("/auth/create-recipe")}
           class="inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-red-500 hover:bg-red-400 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500">
            <svg class="-ml-1 mr-2 h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                <path fill-rule="evenodd" d="M10 3a1 1 0 011 1v5h5a1 1 0 110 2h-5v5a1 1 0 11-2 0v-5H4a1 1 0 110-2h5V4a1 1 0 011-1z" clip-rule="evenodd" />
            </svg>
            Create Recipe
        </a>
    </div>
    {/if}
</div>
