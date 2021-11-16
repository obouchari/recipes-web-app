<script>
    import RecipeList from '$lib/RecipeList.svelte';
    import RecipeCard from '$lib/RecipeCard.svelte';

    let recipes = [];
</script>

<svelte:head>
    <title>Spicety</title>
</svelte:head>

<RecipeList title="Featured Recipes" isEmpty={recipes.length}>
    {#each recipes as recipe}
        <RecipeCard/>
    {/each}
</RecipeList>

<RecipeList title="Recently Added" isEmpty={recipes.length}>
    {#each recipes as recipe}
        <RecipeCard/>
    {/each}
</RecipeList>
