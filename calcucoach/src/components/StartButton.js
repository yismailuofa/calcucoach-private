export default function StartButton(props) {
  return (
    <button
      style={{
        marginTop: "1vh",
        marginBottom: "-1vh",
        fontSize: "3vh",
        letterSpacing: "-0.06em",
        textDecoration: "none",
        fontFamily: "Poppins",
        backgroundColor: "white",
        border: "none",
        cursor: "pointer",
        color: "#4a86ba",
        display: "flex",
        justifyContent: "center",
        borderRadius: "30px",
        height: "100%",
      }}
      onClick={() => {console.log("joon")}}
    >
      Start Your Journey
    </button>
  );
}
