<script>
    export let bookmarked
    export let small

    let bookmarkClasses = small ? "h-5 w-5" : "h-6 w-6"
</script>

<button class="inline-flex items-center p-2 border border-transparent rounded-full shadow-sm bg-gray-200 hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-yellow-500 {!small && 'focus:ring-offset-2'}">
    {#if bookmarked}
        <svg xmlns="http://www.w3.org/2000/svg" class="{bookmarkClasses} text-yellow-500" fill="currentColor" viewBox="0 0 24 24" stroke="none">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z" />
        </svg>
    {:else}
        <svg xmlns="http://www.w3.org/2000/svg" class="{bookmarkClasses} text-gray-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z" />
        </svg>
    {/if}
</button>