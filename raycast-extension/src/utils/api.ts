/*
 * Utility functions for communicating with your backend service.  These
 * functions wrap `fetch` and allow commands to call the Housing Policy
 * Assistant API defined in `settings.yaml`.  To use these functions, set
 * the `assistant_base_url` in your settings file and expose endpoints
 * such as `/add_source`, `/generate_section` and `/sweep_bills` on your own
 * server.
 */

import fetch from "node-fetch";

export const API_BASE_URL = process.env.ASSISTANT_BASE_URL || "http://localhost:8000";

export async function addSource(payload: { title: string; url: string; notes?: string }): Promise<any> {
  const res = await fetch(`${API_BASE_URL}/add_source`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(text || res.statusText);
  }
  return res.json();
}

export async function generateSection(payload: { section: string; prompt: string }): Promise<any> {
  const res = await fetch(`${API_BASE_URL}/generate_section`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(text || res.statusText);
  }
  return res.json();
}

export async function sweepBills(payload: { jurisdictions?: string[]; since?: string }): Promise<any> {
  const res = await fetch(`${API_BASE_URL}/sweep_bills`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(text || res.statusText);
  }
  return res.json();
}