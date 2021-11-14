<script>
	import { url, isActive } from '@roxi/routify'

	export let name
	export let path

	const activeClasses = "bg-red-500 text-white";
	const inactiveClasses = "text-gray-800 hover:bg-yellow-500 hover:bg-opacity-75";
</script>


<a href={$url(path)}
   class="{$isActive(path) ? activeClasses : inactiveClasses} rounded-md py-2 px-3 text-sm font-medium focus:outline-none focus:ring-2 focus:ring-yellow-100"
   aria-current="page">
	{name}
</a>
