function LinkGen() {

  function invite_guest(e) {
    e.preventDefault();
    console.log(e);
  }


  return (
    <div className="container neu-inset">
      <input name="guest" className="neu-inset" type="email" placeholder="enter email"></input>
      <button name="linkgen" className="neu-outset" onClick={invite_guest}>Invite</button>
    </div>
  );
}

export default LinkGen;