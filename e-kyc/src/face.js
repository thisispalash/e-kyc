function VerifyFace() {

  function upload_snippet(e) {
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
        <div className="cell wd-eq neu-inset" id="capture-l">
          50% frames here
        </div>
        <div className="cell wd-mid neu-outset" id="doc-container">
          Instruct user here
        </div>
        <div className="cell wd-eq neu-inset" id="capture-r">
          remaining frames here
        </div>
      </div>
    </div>
  )
}

function AllDone() {

  function upload_document(e) {
    // works client-side
    e.preventDefault();
  }

  function email_data(e) {
    e.preventDefault();

    erase_data();
  }

  function disconnect(e) {
    e.preventDefault();

    erase_data();
  }

  function erase_data() {

  }

  return (
    <div className="container vert-flex neu-inset">
      <div className="row ht-bg" id="vid-row">
        <div className="cell wd-eq neu-inset" id="vid-host">
          Host Video
        </div>
        <div className="cell wd-eq neu-inset" id="vid-guest">
          Guest Video
        </div>
      </div>
      <div className="row ht-sm">
        <div className="cell wd-eq"></div>
        <div className="row vert-flex wd-mid" id="doc-container">
          <button name="upload" className="cell-cent neu-outset" onClick={email_data}>Email Data</button>
          <button name="upload" className="cell-cent neu-outset" onClick={disconnect}>Disconnect</button>
        </div>
        <div className="cell wd-eq"></div>
      </div>
    </div>
  )
}

export { VerifyFace, AllDone };
