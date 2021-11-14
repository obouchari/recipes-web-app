<script>
	import {url} from "@roxi/routify";
	import {truncate} from "$utils/str_utils";
	import BookmarkButton from "$lib/BookmarkButton.svelte";

	export let name = "Spicy Octopus Stir-Fry with"
	export let owner = "Omar David"
	export let rating = 4.5
	export let duration = "15 MIN"
	export let difficulty = "Medium"
</script>


<div class="group relative bg-white rounded-lg flex flex-col overflow-hidden shadow-md">
	<!-- Bookmark recipe -->
	<div class="absolute right-2 top-2 z-20">
		<BookmarkButton small />
	</div>
	<div class="aspect-w-3 aspect-h-2 bg-gray-200 group-hover:opacity-75 sm:aspect-none sm:h-44">
		<img src="https://images.unsplash.com/photo-1476224203421-9ac39bcb3327?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=2070&q=80" alt="food" class="w-full h-full object-center object-cover sm:w-full sm:h-full">
	</div>
	<div class="flex-1 p-4 space-y-2 flex flex-col">
		<div class="flex mb-4">
			<div class="mr-3 flex-shrink-0 self-center">
				<img class="rounded-full h-9 w-9"
					 src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
					 alt="">
			</div>
			<div>
				<h3 class="font-bold">
					<a href={$url("/recipe/:name", {name: "spicy-octopus-stir-fry"})}>
						<span aria-hidden="true" class="absolute inset-0"></span>
						{truncate(name, 20)}
					</a>
				</h3>
				<p class="text-sm text-gray-400">By {owner}</p>
			</div>
		</div>

		<div class="flex-1 flex justify-between items-center">
			<div class="flex items-center space-x-1">
				<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-yellow-400" fill="currentColor" viewBox="0 0 24 24" stroke="currentColor">
					<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
				</svg>
				<p class="text-sm text-gray-600">{rating}</p>
			</div>

			<hr class="border-l border-gray-2 00 h-4"/>

			<div class="flex items-center space-x-1">
				<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
					<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
				</svg>
				<p class="text-sm text-gray-600">{duration}</p>
			</div>

			<hr class="border-l border-gray-200 h-4"/>

			<div>
				<p class="text-sm text-gray-600 uppercase">{difficulty}</p>
			</div>
		</div>
	</div>
</div>