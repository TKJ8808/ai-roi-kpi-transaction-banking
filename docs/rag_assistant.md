# RAG-Based Operations Assistant

## Objective
To support transaction banking operations teams by retrieving relevant
standard operating procedures (SOPs) and past case knowledge during investigations.

## Scope
- Read-only decision support
- No autonomous actions
- No customer interaction

## Approach
- Embed operational documents using sentence embeddings
- Perform similarity-based retrieval
- Present retrieved knowledge to human operators

## Business Value
- Faster investigations
- Reduced dependency on manual SOP lookup
- Consistent operational decision-making

## Responsible AI Controls
- Human-in-the-loop decision making
- Explainable document retrieval
- Full auditability of queries and sources
