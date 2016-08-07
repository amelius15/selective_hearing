import 'babel-polyfill'
import React from 'react'
import ReactDOM from 'react-dom'
import { createStore, applyMiddleware } from 'redux'
import { Provider } from 'react-redux'
import { Router, Route, IndexRoute, browserHistory } from 'react-router'
import { syncHistoryWithStore, routerReducer, routerMiddleware } from 'react-router-redux'

import reducers from './reducers'
import App from './app'
import HearingContainer from './views/hearingContainer'

////////////////////////////////////////////////////////////////////////////////
// Redux Store initialization
////////////////////////////////////////////////////////////////////////////////

let store = createStore(reducers, applyMiddleware(routerMiddleware(browserHistory)))

////////////////////////////////////////////////////////////////////////////////
// Render the DOM
////////////////////////////////////////////////////////////////////////////////

let rootElement = document.getElementById('container')

const syncedHistory = syncHistoryWithStore(browserHistory, store, {
    selectLocationState: (state) => state.get('routing').toJS()
})

ReactDOM.render(
    <Provider store={store}>
        <Router history={syncedHistory}>
            <Route path="/" components={App}>
                <IndexRoute component={HearingContainer} />
            </Route>
        </Router>
    </Provider>,
    rootElement
)
