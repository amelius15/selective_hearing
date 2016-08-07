import React, { Component, PropTypes } from 'react'

const App = (props) =>{
    return (
        <div className="wrapper">
            { props.children }
        </div>
    )
}

App.propTypes = {
    children: PropTypes.oneOfType([
        PropTypes.arrayOf(PropTypes.element),
        PropTypes.element
    ])
}

export default App
