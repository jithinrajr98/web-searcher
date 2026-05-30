import { useState } from "react";
import SearchBar from "./components/SearchBar";
import Report from "./components/Report";
import Sources from "./components/Sources";
import { research } from "./api";
import type { ResearchResponse } from "./types";

export default function App() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [result, setResult] = useState<ResearchResponse | null>(null);

  async function handleSearch(query: string) {
    setLoading(true);
    setError("");
    setResult(null);
    try {
      const data = await research(query);
      setResult(data);
    } catch (e) {
      setError(e instanceof Error ? e.message : "Something went wrong");
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="app">
      <h1>Web Searcher</h1>
      <p className="subtitle">Search the web and get a concise report.</p>

      <SearchBar onSearch={handleSearch} loading={loading} />

      {error && <p className="error">{error}</p>}
      {loading && <p className="status">Searching the web and writing your report...</p>}

      {result && (
        <>
          <Report report={result.report} />
          <Sources sources={result.sources} />
        </>
      )}
    </main>
  );
}
