import React, { Component, PropTypes } from 'react'

export default class FireButton extends Component {
    render() {
        return (
            <svg className="fireButton">
                <polygon points="70, 55 70, 145 145, 100" fill="#fff"/>
            </svg>
        )
    }
}
