from inui.elements import *
from inui.svg import *

Html(
    data=(
        Body(
            data=(
                Header(
                    id="""header""", classs="""topbar-sticky-shrink-header""", data=()
                ),
                Div(
                    data_sticky_container="",
                    data=(
                        Div(
                            data_sticky="",
                            data_margin_top="""0""",
                            data_top_anchor="""header:bottom""",
                            data_btm_anchor="""content:bottom""",
                            data=(
                                Div(
                                    classs="""top-bar topbar-sticky-shrink""",
                                    data=(
                                        Div(
                                            classs="""top-bar-title""",
                                            data=(
                                                Img(
                                                    src="""https://placehold.it/150x38""",
                                                    alt="",
                                                ),
                                            ),
                                        ),
                                        Div(
                                            classs="""top-bar-right""",
                                            data=(
                                                Ul(
                                                    classs="""menu""",
                                                    data=(
                                                        Li(
                                                            data=(
                                                                A(
                                                                    href="""#""",
                                                                    data=(
                                                                        """Thing 1""",
                                                                    ),
                                                                ),
                                                            )
                                                        ),
                                                        Li(
                                                            data=(
                                                                A(
                                                                    href="""#""",
                                                                    data=(
                                                                        """Thing 2""",
                                                                    ),
                                                                ),
                                                            )
                                                        ),
                                                        Li(
                                                            data=(
                                                                A(
                                                                    href="""#""",
                                                                    data=(
                                                                        """Thing 3""",
                                                                    ),
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
                Br(),
                Div(
                    classs="""column row""",
                    id="""content""",
                    data=(
                        H3(
                            classs="""text-center""",
                            data=(
                                """Creating a sticky Navigation Menu with Top Bar!""",
                            ),
                        ),
                        Img(
                            src="""https://placehold.it/1200x300&text=content/100""",
                        ),
                        Img(
                            src="""https://placehold.it/1200x300&text=content/200""",
                        ),
                        Img(
                            src="""https://placehold.it/1200x300&text=content/300""",
                        ),
                        Img(
                            src="""https://placehold.it/1200x300&text=content/400""",
                        ),
                        Img(
                            src="""https://placehold.it/1200x300&text=content/500""",
                        ),
                        Img(
                            src="""https://placehold.it/1200x300&text=content/600""",
                        ),
                    ),
                ),
            )
        ),
    )
)
