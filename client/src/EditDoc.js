import React, { Component } from 'react' // React for JSX

/*
 *
 */
class EditDoc extends Component {

  state = {

  }
  
  render() {
    
    const {name, dob, address, relation} = this.props
    
    return (
      <div className='container' >
        <div className='doc-view' >

        </div>

        <div className='form-edit' >

        </div>
      </div>
    )
    
  }
}