function DocUpload() {

  function upload_document(e) {
    // works client-side
    e.preventDefault();
  }

  return (
    <div className="container vert-flex neu-inset">
      <div className="row ht-sm" id="vid-row">
        <div className="cell wd-eq neu-inset" id="vid-host">
          Host Video
        </div>
        <div className="cell wd-eq neu-inset" id="vid-guest">
          Guest Video
        </div>
      </div>
      <div className="row ht-bg" id="dat-row">
        <div className="cell wd-eq"></div>
        <div className="cell wd-mid neu-inset" id="doc-container">
          Upload doc here
          <button name="upload" className="neu-outset" onClick={upload_document}>Upload</button>
        </div>
        <div className="cell wd-eq"></div>
      </div>
    </div>
  )
}

function DataUpload() {

  function submit_data(e) {

  }

  return (
    <div className="container vert-flex neu-inset">
      <div className="row ht-sm" id="vid-row">
        <div className="cell wd-eq neu-inset" id="vid-host">
          Host Video
        </div>
        <div className="cell wd-eq neu-inset" id="vid-guest">
          Guest Video
        </div>
      </div>
      <div className="row ht-bg" id="dat-row">
        <div className="cell wd-big neu-inset" id="doc-container"></div>
        <div className="cell vert-flex wd-eq neu-outset" id="data-container">
          <div className="cell ht-sm" id="data-key">
            <label className="neu-inset" id="data-key" for="data">label</label>
          </div>
          <div className="cell ht-sm">
            <input id="data" name="data-value" className="neu-inset" type="text"></input>
          </div>
          <div className="cell ht-sm">
            <button name="upload" className="neu-outset" onClick={submit_data}>Submit</button>
          </div>
        </div>
      </div>
    </div>
  );
}


export { DocUpload, DataUpload };