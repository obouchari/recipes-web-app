<script>
    import { params } from "@roxi/routify"
    import Rating from "$lib/Rating.svelte";
    import BookmarkButton from "$lib/BookmarkButton.svelte";

    console.log($params)
</script>


<div>
    <div class="mx-auto relative py-16 px-4 sm:py-16 sm:px-6 lg:max-w-7xl lg:px-8">
        <!-- Bookmark recipe -->
        <div class="absolute right-5 top-5">
            <BookmarkButton bookmarked/>
        </div>
        <!-- Recipe -->
        <div class="lg:grid lg:grid-rows-1 lg:grid-cols-7 lg:gap-x-8 lg:gap-y-10 xl:gap-x-16">
            <!-- Recipe image -->
            <div class="lg:row-end-1 lg:col-span-4">
                <div class="aspect-w-4 aspect-h-3 rounded-lg bg-gray-100 overflow-hidden">
                    <img src="https://images.unsplash.com/photo-1596189181426-7f63a1737f0d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=2070&q=80" alt="food pic" class="object-center object-cover">
                </div>
            </div>

            <!-- Recipe details -->
            <div class="max-w-2xl mx-auto mt-14 sm:mt-16 lg:max-w-none lg:mt-0 lg:row-end-2 lg:row-span-2 lg:col-span-3">
                <div class="flex flex-col-reverse">
                    <div class="mt-4">
                        <h1 class="text-2xl font-extrabold tracking-tight text-gray-900 sm:text-3xl">{$params.name}</h1>

<!--                        <h2 id="information-heading" class="sr-only">Product information</h2>-->
<!--                        <p class="text-sm text-gray-500 mt-2">Version 1.0 (Updated <time datetime="2021-06-05">June 5, 2021</time>)</p>-->
                    </div>

                    <div>
                        <h3 class="sr-only">Reviews</h3>
                        <Rating />
                    </div>
                </div>

                <p class="text-gray-500 mt-6">The Application UI Icon Pack comes with over 200 icons in 3 styles: outline, filled, and branded. This playful icon pack is tailored for complex application user interfaces with a friendly and legible look.</p>

                <div class="mt-10 flex-1 flex justify-evenly sm:justify-start sm:space-x-6 items-center">
                    <div class="flex items-center space-x-1">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                        </svg>
                        <p class="text-sm text-gray-600 uppercase">10 min</p>
                    </div>

                    <hr class="border-l border-gray-300 h-4"/>

                    <div><p class="text-sm text-gray-600 uppercase">Easy</p></div>

                    <hr class="border-l border-gray-300 h-4"/>

                    <div class="flex items-center space-x-1">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
                        </svg>
                        <p class="text-sm text-gray-600 uppercase">2 serving</p>
                    </div>
                </div>

                <div class="border-t border-gray-200 mt-10 pt-10">
                    <h3 class="text-sm font-medium text-gray-900">Ingredients</h3>
                    <div class="mt-4 prose prose-sm text-gray-500">
                        <ul role="list">
                            <li>200+ SVG icons in 3 unique styles</li>
                            <li>Compatible with Figma, Sketch, and Adobe XD</li>
                            <li>Drawn on 24 x 24 pixel grid</li>
                        </ul>
                    </div>
                </div>

                <div class="border-t border-gray-200 mt-10 pt-10">
                    <h3 class="text-sm font-medium text-gray-900">Instructions</h3>
                    <p class="mt-4 text-sm text-gray-500">For personal and professional use. You cannot resell or redistribute these icons in their original or modified state. <a href="#" class="font-medium text-indigo-600 hover:text-indigo-500">Read full license</a></p>
                </div>

                <div class="border-t border-gray-200 mt-10 pt-10">
                    <h3 class="text-sm font-medium text-gray-900">Share</h3>
                    <ul role="list" class="flex items-center space-x-6 mt-4">
                        <li>
                            <a href="#" class="flex items-center justify-center w-6 h-6 text-gray-400 hover:text-gray-500">
                                <span class="sr-only">Share on Facebook</span>
                                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" aria-hidden="true">
                                    <path fill-rule="evenodd" d="M20 10c0-5.523-4.477-10-10-10S0 4.477 0 10c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V10h2.54V7.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V10h2.773l-.443 2.89h-2.33v6.988C16.343 19.128 20 14.991 20 10z" clip-rule="evenodd" />
                                </svg>
                            </a>
                        </li>
                        <li>
                            <a href="#" class="flex items-center justify-center w-6 h-6 text-gray-400 hover:text-gray-500">
                                <span class="sr-only">Share on Instagram</span>
                                <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                                    <path fill-rule="evenodd" d="M12.315 2c2.43 0 2.784.013 3.808.06 1.064.049 1.791.218 2.427.465a4.902 4.902 0 011.772 1.153 4.902 4.902 0 011.153 1.772c.247.636.416 1.363.465 2.427.048 1.067.06 1.407.06 4.123v.08c0 2.643-.012 2.987-.06 4.043-.049 1.064-.218 1.791-.465 2.427a4.902 4.902 0 01-1.153 1.772 4.902 4.902 0 01-1.772 1.153c-.636.247-1.363.416-2.427.465-1.067.048-1.407.06-4.123.06h-.08c-2.643 0-2.987-.012-4.043-.06-1.064-.049-1.791-.218-2.427-.465a4.902 4.902 0 01-1.772-1.153 4.902 4.902 0 01-1.153-1.772c-.247-.636-.416-1.363-.465-2.427-.047-1.024-.06-1.379-.06-3.808v-.63c0-2.43.013-2.784.06-3.808.049-1.064.218-1.791.465-2.427a4.902 4.902 0 011.153-1.772A4.902 4.902 0 015.45 2.525c.636-.247 1.363-.416 2.427-.465C8.901 2.013 9.256 2 11.685 2h.63zm-.081 1.802h-.468c-2.456 0-2.784.011-3.807.058-.975.045-1.504.207-1.857.344-.467.182-.8.398-1.15.748-.35.35-.566.683-.748 1.15-.137.353-.3.882-.344 1.857-.047 1.023-.058 1.351-.058 3.807v.468c0 2.456.011 2.784.058 3.807.045.975.207 1.504.344 1.857.182.466.399.8.748 1.15.35.35.683.566 1.15.748.353.137.882.3 1.857.344 1.054.048 1.37.058 4.041.058h.08c2.597 0 2.917-.01 3.96-.058.976-.045 1.505-.207 1.858-.344.466-.182.8-.398 1.15-.748.35-.35.566-.683.748-1.15.137-.353.3-.882.344-1.857.048-1.055.058-1.37.058-4.041v-.08c0-2.597-.01-2.917-.058-3.96-.045-.976-.207-1.505-.344-1.858a3.097 3.097 0 00-.748-1.15 3.098 3.098 0 00-1.15-.748c-.353-.137-.882-.3-1.857-.344-1.023-.047-1.351-.058-3.807-.058zM12 6.865a5.135 5.135 0 110 10.27 5.135 5.135 0 010-10.27zm0 1.802a3.333 3.333 0 100 6.666 3.333 3.333 0 000-6.666zm5.338-3.205a1.2 1.2 0 110 2.4 1.2 1.2 0 010-2.4z" clip-rule="evenodd" />
                                </svg>
                            </a>
                        </li>
                        <li>
                            <a href="#" class="flex items-center justify-center w-6 h-6 text-gray-400 hover:text-gray-500">
                                <span class="sr-only">Share on Twitter</span>
                                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" aria-hidden="true">
                                    <path d="M6.29 18.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0020 3.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.073 4.073 0 01.8 7.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 010 16.407a11.616 11.616 0 006.29 1.84" />
                                </svg>
                            </a>
                        </li>
                    </ul>
                </div>
            </div>

            <div class="w-full max-w-2xl mx-auto mt-16 lg:max-w-none lg:mt-0 lg:col-span-4">
                <div>
                    <h3 class="border-b border-gray-200 pb-4 flex">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-gray-600 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8h2a2 2 0 012 2v6a2 2 0 01-2 2h-2v4l-4-4H9a1.994 1.994 0 01-1.414-.586m0 0L11 14h4a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2v4l.586-.586z" />
                        </svg>
                        Comments and Reviews
                    </h3>

                    <!-- Comments and Reviews -->
                    <div id="tab-panel-reviews" class="-mb-10" aria-labelledby="tab-reviews" role="tabpanel" tabindex="0">
                        <h3 class="sr-only">Customer Reviews</h3>

                        <div class="flex text-sm text-gray-500 space-x-4">
                            <div class="flex-none py-10">
                                <img src="https://images.unsplash.com/photo-1502685104226-ee32379fefbe?ixlib=rb-=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=8&w=256&h=256&q=80" alt="" class="w-10 h-10 bg-gray-100 rounded-full">
                            </div>
                            <div class="py-10">
                                <h3 class="font-medium text-gray-900">Emily Selman</h3>
                                <p><time datetime="2021-07-16">July 16, 2021</time></p>

                                <Rating classes="mt-4"/>

                                <div class="mt-4 prose prose-sm max-w-none text-gray-500">
                                    <p>This icon pack is just what I need for my latest project. There's an icon for just about anything I could ever need. Love the playful look!</p>
                                </div>
                            </div>
                        </div>

                        <div class="flex text-sm text-gray-500 space-x-4">
                            <div class="flex-none py-10">
                                <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=8&w=256&h=256&q=80" alt="" class="w-10 h-10 bg-gray-100 rounded-full">
                            </div>
                            <div class="py-10 border-t border-gray-200">
                                <h3 class="font-medium text-gray-900">Hector Gibbons</h3>
                                <p><time datetime="2021-07-12">July 12, 2021</time></p>

                                <Rating classes="mt-4"/>

                                <div class="mt-4 prose prose-sm max-w-none text-gray-500">
                                    <p>Blown away by how polished this icon pack is. Everything looks so consistent and each SVG is optimized out of the box so I can use it directly with confidence. It would take me several hours to create a single icon this good, so it's a steal at this price.</p>
                                </div>
                            </div>
                        </div>

                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
