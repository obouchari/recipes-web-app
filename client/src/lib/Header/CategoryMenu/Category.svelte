<script>
    import {url} from "@roxi/routify";

    export let icon
    export let title
    export let description
    export let category
</script>

<a href={$url("/recipes", {category})}
   class="-m-3 p-3 flex items-start rounded-lg hover:bg-gray-50 transition ease-in-out duration-150"
   on:click>
    <div class="flex-shrink-0 flex items-center justify-center h-10 w-10 rounded-md bg-yellow-400 text-gray-700 sm:h-12 sm:w-12">
        <img class="block h-8 w-8" src={icon} alt="Main Dish">
    </div>
    <div class="ml-4">
        <p class="text-base font-medium text-gray-900">
            {title}
        </p>
        <p class="mt-1 text-sm text-gray-500">
            {description}
        </p>
    </div>
</a>