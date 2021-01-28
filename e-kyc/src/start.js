function HostEnter() { /* TODO demo */ }

function LinkGen() {

  function invite_guest(e) {
    // works client-side
    e.preventDefault();

  }

  return (
    <div className="container vert-flex neu-inset">
      <div className="row ht-sm">
        <input name="guest" className="cell-cent neu-inset" type="email" placeholder="enter guest email"></input>
        <button name="linkgen" className="cell-cent neu-outset" onClick={invite_guest}>Invite</button>
      </div>
    </div>
  );
}

export { HostEnter, LinkGen };