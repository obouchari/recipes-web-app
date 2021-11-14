<script>
    import RecipeList from '$lib/RecipeList.svelte';
    import RecipeCard from '$lib/RecipeCard.svelte';

    let recipes = [1,2,3,4];
</script>

<svelte:head>
    <title>Spicety</title>
</svelte:head>


<RecipeList title="Featured Recipes">
    {#each recipes as recipe}
        <RecipeCard/>
    {/each}
</RecipeList>

<RecipeList title="Recently Added">
    {#each recipes as recipe}
        <RecipeCard/>
    {/each}
</RecipeList>
