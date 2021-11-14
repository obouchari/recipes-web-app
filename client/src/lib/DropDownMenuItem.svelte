<script>
    import {url} from "@roxi/routify";

    export let name
    export let path
</script>

<a href={$url(path)} class="block py-2 px-4 text-sm text-gray-700 hover:bg-gray-100" role="menuitem"
   tabindex="-1">
    {name}
</a>