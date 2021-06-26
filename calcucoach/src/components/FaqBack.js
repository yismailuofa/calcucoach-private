export default function FaqBack({faqHide}) {
  return (
    <div>
      <button
        style={{
          marginTop: "4vh",
          marginBottom: "-1vh",
          fontSize: "3vh",
          padding: "1.5vh",
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
        }}
        onClick={faqHide}
      >
        Go Back
      </button>
    </div>
  );
}
