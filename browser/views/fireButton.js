import React, { Component, PropTypes } from 'react'

export default class FireButton extends Component {
    render() {
        return (
            <svg className="fireButton" onClick={ this.props.handleClick }>
                <polygon points="70, 55 70, 145 145, 100" fill="#fff"/>
            </svg>
        )
    }
}

FireButton.propTypes = {
    handleClick: PropTypes.func.isRequired
}
