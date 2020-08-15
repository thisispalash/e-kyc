import React, { Component } from 'react' // React for JSX

/*
 *
 */
class SelectDoc extends Component {

  state = {
    name: getNameDims(),
    dob: getDOBDims(),
    addr: getAddressDims(),
    rel: getRelationsDims(),
  }
  
  getNameDims = () => {
    
    return null
  }
  
  getDOBDims = () => {
    
    return null
  }
  
  getAddressDims = () => {
    
    return null
  }
  
  getRelationsDims = () => {
    
    return null
  }

  render() {
    
    const { file } = this.props
    
    return (
      <div className='' >

      </div>
    )
    
  }
}

export default SelectDoc