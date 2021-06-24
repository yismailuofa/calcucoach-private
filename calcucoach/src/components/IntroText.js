export default function IntroText() {
  return (
    <div
      style={{
        fontSize: "5vh",
        background: "#4a86ba",
        padding: "4vh",
        paddingTop: "2vh",
        borderRadius: "30px",
        display: "flex",
        flexDirection: "column",
        position: "relative",
        justifyText: "center"
      }}
    >
      Free training.<br/>Made for you.
      <a
        href="."
        style={{
          marginTop: "1vh",
          marginBottom: "-1vh",
          fontSize: "3vh",
          letterSpacing: "-0.06em",
          textDecoration: "none",
          color: "#4a86ba",
          background: "white",
          display: "flex",
          justifyContent: "center",
          borderRadius: "30px",
          height: "100%"
        }}
      >
        Start Your Journey
      </a>  
    </div>
  );
}
