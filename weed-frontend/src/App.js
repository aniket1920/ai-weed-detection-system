import React, { useState } from "react";
import axios from "axios";

function App() {
  const [image, setImage] = useState(null);
  const [resultImage, setResultImage] = useState(null);
  const [weedCount, setWeedCount] = useState(null);
  const [processingTime, setProcessingTime] = useState(null);
  const [confidence, setConfidence] = useState(0.25);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!image) return;

    const formData = new FormData();
    formData.append("file", image);

    setLoading(true);

    try {
      const response = await axios.post(
        `https://akhand2210093-weed-detection-api.hf.space/predict?conf=${confidence}`,
        formData,
        { responseType: "blob" }
      );

      const imageUrl = URL.createObjectURL(response.data);
      setResultImage(imageUrl);

      setWeedCount(response.headers["x-weed-count"]);
      setProcessingTime(response.headers["x-processing-time-ms"]);
    } catch (error) {
      console.error(error);
    }

    setLoading(false);
  };

  return (
    <div className="bg-[#F5F1E6]">

      {/* HERO SECTION */}
      <div
        className="h-screen bg-cover bg-center flex flex-col justify-center items-center text-white text-center px-6"
        style={{
          backgroundImage:
            "linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.55)), url('https://images.unsplash.com/photo-1500937386664-56d1dfef3854')",
        }}
      >
        <h1 className="text-5xl font-bold mb-6">
          🌾 Smart Weed Detection for Farmers
        </h1>

        <p className="text-xl max-w-2xl mb-8">
          AI-powered crop monitoring system designed to detect harmful weeds
          instantly from field images and support precision agriculture.
        </p>

        <a
          href="#detect"
          className="bg-green-600 px-8 py-3 rounded-lg text-lg font-semibold hover:bg-green-700 transition duration-300"
        >
          🌱 Start Field Analysis
        </a>
      </div>

      {/* FEATURES SECTION */}
      <div className="py-16 px-8 text-center">
        <h2 className="text-3xl font-bold text-green-800 mb-10">
          Why Use This System?
        </h2>

        <div className="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto">
          <div className="bg-white p-6 rounded-2xl shadow-lg">
            <h3 className="text-xl font-semibold mb-2">🌱 Accurate Detection</h3>
            <p>Trained using deep learning models for reliable weed identification.</p>
          </div>

          <div className="bg-white p-6 rounded-2xl shadow-lg">
            <h3 className="text-xl font-semibold mb-2">⚡ Fast Processing</h3>
            <p>Provides results in milliseconds for real-time field decisions.</p>
          </div>

          <div className="bg-white p-6 rounded-2xl shadow-lg">
            <h3 className="text-xl font-semibold mb-2">📱 Easy to Use</h3>
            <p>Simple interface designed for farmers and agricultural workers.</p>
          </div>
        </div>
      </div>

      {/* DETECTION SECTION */}
      <div id="detect" className="py-16 px-6 flex flex-col items-center">

        <div className="bg-white shadow-xl rounded-2xl p-8 w-full max-w-xl">
          <h2 className="text-2xl font-bold text-green-800 mb-4 text-center">
            📷 Upload Field Image
          </h2>

          <input
            type="file"
            className="mb-4 w-full"
            onChange={(e) => setImage(e.target.files[0])}
          />

          <label className="block font-medium text-gray-700 mb-2">
            Confidence: {confidence}
          </label>

          <input
            type="range"
            min="0.1"
            max="0.9"
            step="0.05"
            value={confidence}
            onChange={(e) => setConfidence(e.target.value)}
            className="w-full mb-4"
          />

          <button
            onClick={handleUpload}
            disabled={loading}
            className="w-full bg-green-600 text-white py-3 rounded-lg hover:bg-green-700 transition duration-300"
          >
            {loading ? "Analyzing Field..." : "🌱 Analyze Field"}
          </button>
        </div>

        {/* RESULT */}
        {resultImage && (
          <div className="mt-12 bg-white shadow-xl rounded-2xl p-6 max-w-3xl text-center">
            <h2 className="text-2xl font-bold text-green-800 mb-4">
              Detection Result
            </h2>

            <img
              src={resultImage}
              alt="Result"
              className="rounded-xl mx-auto mb-6"
            />

            <div className="flex justify-around text-lg font-medium text-gray-700">
              <div>
                🌱 Weed Count
                <p className="text-3xl text-green-800 font-bold">
                  {weedCount}
                </p>
              </div>

              <div>
                ⏱ Processing Time
                <p className="text-3xl text-green-800 font-bold">
                  {processingTime} ms
                </p>
              </div>
            </div>
          </div>
        )}
      </div>

    </div>
  );
}

export default App;