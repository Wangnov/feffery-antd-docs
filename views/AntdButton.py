import dash_html_components as html
import dash_core_components as dcc
import feffery_antd_components as fac

import callbacks.AntdButton

docs_content = html.Div(
    [
        html.H2(
            'AntdButton(children, id, className, style, **kwargs)',
            style={
                'borderLeft': '4px solid grey',
                'padding': '3px 0 3px 10px',
                'backgroundColor': '#f5f5f5'
            }
        ),

        fac.AntdAnchor(
            linkDict=[
                {'title': '主要参数说明', 'href': '#主要参数说明'},
                {
                    'title': '使用示例',
                    'href': '#使用示例',
                    'children': [
                        {'title': '不同type对应按钮样式风格', 'href': '#不同type对应按钮样式风格'},
                        {'title': '充当跳转功能使用', 'href': '#充当跳转功能使用'},
                        {'title': '撑满父级元素宽度', 'href': '#撑满父级元素宽度'},
                        {'title': '显示为危险警告状态', 'href': '#显示为危险警告状态'},
                        {'title': '显示为不可点击状态', 'href': '#显示为不可点击状态'},
                        {'title': '修改按钮形状', 'href': '#修改按钮形状'},
                        {'title': '回调示例', 'href': '#回调示例'},
                    ]
                },
            ],
            containerId='docs-content',
            targetOffset=200
        ),
        html.Span(
            '主要参数说明',
            id='#主要参数说明',
            style={
                'borderLeft': '4px solid grey',
                'padding': '3px 0 3px 10px',
                'backgroundColor': '#f5f5f5',
                'fontWeight': 'bold',
                'fontSize': '1.2rem'
            }
        ),

        dcc.Markdown(open('documents/AntdButton.md', encoding='utf-8').read(),
                     dangerously_allow_html=True),

        html.Div(
            html.Span(
                '使用示例',
                id='使用示例',
                style={
                    'borderLeft': '4px solid grey',
                    'padding': '3px 0 3px 10px',
                    'backgroundColor': '#f5f5f5',
                    'fontWeight': 'bold',
                    'fontSize': '1.2rem'
                }
            ),
            style={
                'marginBottom': '10px'
            }
        ),

        html.Div(
            [
                html.Div(
                    [
                        fac.AntdButton('default'),
                        fac.AntdButton('primary', type='primary'),
                        fac.AntdButton('dashed', type='dashed'),
                        fac.AntdButton('link', type='link'),
                        fac.AntdButton('text', type='text')
                    ]
                ),

                fac.AntdDivider(
                    '不同type对应按钮样式风格',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdPopover(
                    [
                        fac.AntdButton('点击查看代码', type='link'),

                        dcc.Markdown('''
                ```Python
                html.Div(
                    [
                        fac.AntdButton('default'),
                        fac.AntdButton('primary', type='primary'),
                        fac.AntdButton('dashed', type='dashed'),
                        fac.AntdButton('link', type='link'),
                        fac.AntdButton('text', type='text')
                    ]
                )
                ```
                ''')
                    ],
                    contentChildrenIndexes=[1],
                    placement='rightTop',
                    trigger='click',
                    containerId='docs-content'
                )

            ],
            style={
                'marginBottom': '40px',
                'padding': '10px 10px 20px 10px',
                'border': '1px solid #f0f0f0'
            },
            id='不同type对应按钮样式风格',
            className='div-highlight'
        ),

        html.Div(
            [
                fac.AntdButton('feffery-antd-components',
                               href='https://github.com/CNFeffery/feffery-antd-components',
                               target='_blank',
                               type='primary'),

                fac.AntdDivider(
                    '充当跳转功能使用',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdPopover(
                    [
                        fac.AntdButton('点击查看代码', type='link'),

                        dcc.Markdown('''
                                        ```Python
                                        fac.AntdButton(href='https://github.com/CNFeffery/feffery-antd-components',
                                                       target='_blank')
                                        ```
                                        '''),
                    ],
                    contentChildrenIndexes=[1],
                    placement='rightTop',
                    trigger='click',
                    containerId='docs-content'
                )

            ],
            id='充当跳转功能使用',
            style={
                'marginBottom': '40px',
                'padding': '10px 10px 20px 10px',
                'border': '1px solid #f0f0f0'
            },
            className='div-highlight'
        ),

        html.Div(
            [
                fac.AntdButton('feffery-antd-components',
                               block=True,
                               type='primary'),

                fac.AntdDivider(
                    '撑满父级元素宽度',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdPopover(
                    [
                        fac.AntdButton('点击查看代码', type='link'),

                        dcc.Markdown('''
                                        ```Python
                                        fac.AntdButton('feffery-antd-components',
                                                       block=True,
                                                       type='primary')
                                        ```
                                        '''),
                    ],
                    contentChildrenIndexes=[1],
                    placement='rightTop',
                    trigger='click',
                    containerId='docs-content'
                ),

            ],
            id='撑满父级元素宽度',
            style={
                'marginBottom': '40px',
                'padding': '10px 10px 20px 10px',
                'border': '1px solid #f0f0f0'
            },
            className='div-highlight'
        ),

        html.Div(
            [
                html.Div(
                    [
                        fac.AntdButton('default', danger=True),
                        fac.AntdButton('primary', type='primary', danger=True),
                        fac.AntdButton('dashed', type='dashed', danger=True),
                        fac.AntdButton('link', type='link', danger=True),
                        fac.AntdButton('text', type='text', danger=True)
                    ]
                ),

                fac.AntdDivider(
                    '显示为危险警告状态',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdPopover(
                    [
                        fac.AntdButton('点击查看代码', type='link'),

                        dcc.Markdown('''
                                        ```Python
                                        html.Div(
                                            [
                                                fac.AntdButton('default', danger=True),
                                                fac.AntdButton('primary', type='primary', danger=True),
                                                fac.AntdButton('dashed', type='dashed', danger=True),
                                                fac.AntdButton('link', type='link', danger=True),
                                                fac.AntdButton('text', type='text', danger=True)
                                            ]
                                        )
                                        ```
                                        '''),
                    ],
                    contentChildrenIndexes=[1],
                    placement='rightTop',
                    trigger='click',
                    containerId='docs-content'
                )

            ],
            id='显示为危险警告状态',
            style={
                'marginBottom': '40px',
                'padding': '10px 10px 20px 10px',
                'border': '1px solid #f0f0f0'
            },
            className='div-highlight'
        ),

        html.Div(
            [
                html.Div(
                    [
                        fac.AntdButton('default', disabled=True),
                        fac.AntdButton('primary', type='primary', disabled=True),
                        fac.AntdButton('dashed', type='dashed', disabled=True),
                        fac.AntdButton('link', type='link', disabled=True),
                        fac.AntdButton('text', type='text', disabled=True)
                    ]
                ),

                fac.AntdDivider(
                    '显示为不可点击状态',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdPopover(
                    [
                        fac.AntdButton('点击查看代码', type='link'),

                        dcc.Markdown('''
                                        ```Python
                                        html.Div(
                                            [
                                                fac.AntdButton('default', disabled=True),
                                                fac.AntdButton('primary', type='primary', disabled=True),
                                                fac.AntdButton('dashed', type='dashed', disabled=True),
                                                fac.AntdButton('link', type='link', disabled=True),
                                                fac.AntdButton('text', type='text', disabled=True)
                                            ]
                                        )
                                        ```
                                        '''),
                    ],
                    contentChildrenIndexes=[1],
                    placement='rightTop',
                    trigger='click',
                    containerId='docs-content'
                ),

            ],
            id='显示为不可点击状态',
            style={
                'marginBottom': '40px',
                'padding': '10px 10px 20px 10px',
                'border': '1px solid #f0f0f0'
            },
            className='div-highlight'
        ),

        html.Div(
            [

                html.Div(
                    [
                        fac.AntdButton('默认', type='primary'),
                        fac.AntdButton('circle', shape='circle', type='primary'),
                        fac.AntdButton('round', shape='round', type='primary')
                    ]
                ),

                fac.AntdDivider(
                    '修改按钮形状',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdPopover(
                    [
                        fac.AntdButton('点击查看代码', type='link'),

                        dcc.Markdown('''
                                        ```Python
                                        html.Div(
                                            [
                                                fac.AntdButton('默认'),
                                                fac.AntdButton('circle', shape='circle'),
                                                fac.AntdButton('round', shape='round')
                                            ]
                                        )
                                        ```
                                        '''),
                    ],
                    contentChildrenIndexes=[1],
                    placement='rightTop',
                    trigger='click',
                    containerId='docs-content'
                ),

            ],
            id='修改按钮形状',
            style={
                'marginBottom': '40px',
                'padding': '10px 10px 20px 10px',
                'border': '1px solid #f0f0f0'
            },
            className='div-highlight'
        ),

        html.Div(
            [

                fac.AntdButton('点我点我', type='primary', id='button-demo'),
                html.Br(),
                html.Em(id='button-demo-output'),

                fac.AntdDivider(
                    '回调示例',
                    innerTextOrientation='left',
                    lineColor='#f0f0f0'
                ),

                fac.AntdPopover(
                    [
                        fac.AntdButton('点击查看代码', type='link'),

                        dcc.Markdown('''
                                        ```Python
                                        fac.AntdButton('点我点我', type='primary', id='button-demo'),
                                        html.Br(),
                                        html.Em(id='button-demo-output')
                                        ...
                                        @app.callback(
                                            Output('button-demo-output', 'children'),
                                            Input('button-demo', 'nClicks'),
                                            prevent_initial_call=True
                                        )
                                        def button_callback_demo(nClicks):

                                            return nClicks
                                        ```
                                        '''),
                    ],
                    contentChildrenIndexes=[1],
                    placement='rightTop',
                    trigger='click',
                    containerId='docs-content'
                ),

            ],
            id='回调示例',
            style={
                'marginBottom': '80px',
                'padding': '10px 10px 20px 10px',
                'border': '1px solid #f0f0f0'
            },
            className='div-highlight'
        ),

        html.Div(style={'height': '100px'})
    ]
)
