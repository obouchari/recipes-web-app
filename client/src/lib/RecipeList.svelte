<script>
	export let title = ""
</script>




	<div class="max-w-2xl mx-auto py-16 px-4 sm:py-6 sm:px-6 lg:max-w-7xl lg:px-4">

		<!-- This example requires Tailwind CSS v2.0+ -->
		<div class="pb-5 mb-8 border-b border-gray-200 sm:flex sm:items-center sm:justify-between">
			<h3 class="text-2xl font-extrabold tracking-tight sm:text-3xl leading-6 text-gray-900">
				{title}
			</h3>
			<div class="mt-3 sm:mt-0 sm:ml-4">
				<span class="relative z-0 inline-flex shadow-sm rounded-md">
					<button type="button" class="relative inline-flex items-center px-2 py-2 rounded-l-md border border-gray-300 bg-gray-50 text-sm font-medium text-gray-500 hover:bg-gray-100 focus:z-10 focus:outline-none focus:ring-1 focus:ring-yellow-400 focus:border-yellow-400">
						<span class="sr-only">Previous</span>
						<svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
							<path fill-rule="evenodd" d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z" clip-rule="evenodd" />
						</svg>
					</button>
					<button type="button" class="-ml-px relative inline-flex items-center px-2 py-2 rounded-r-md border border-gray-300 bg-gray-50 text-sm font-medium text-gray-500 hover:bg-gray-100 focus:z-10 focus:outline-none focus:ring-1 focus:ring-yellow-400 focus:border-yellow-400">
						<span class="sr-only">Next</span>
						<svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
							<path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" />
						</svg>
					</button>
				</span>

			</div>
		</div>

		<div class="grid grid-cols-1 gap-y-4 sm:grid-cols-2 sm:gap-x-6 sm:gap-y-12 lg:grid-cols-4 lg:gap-x-8">
			<slot/>
		</div>
	</div>
