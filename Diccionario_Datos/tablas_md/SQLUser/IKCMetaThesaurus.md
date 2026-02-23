# SQLUser.IKCMetaThesaurus

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| AUI | varchar |  |  | SI | Unique Identifier for atom |
| CUI | varchar |  |  | SI | Concept Unique Identifier |
| LAT | varchar |  |  | SI | Language of Term |
| LUI | varchar |  |  | SI | Unique Identifier for Term |
| SAB | varchar |  |  | SI | Source Vocabulary |
| STR | varchar |  |  | SI | String |
| STRShort | varchar |  |  | SI | Same as STR but length limited to 250 for indexing... |
| STRWordLength | integer |  |  | SI | Computed number of words in the normalised string |
| STT | varchar |  |  | SI | String Type |
| SUI | varchar |  |  | SI | Unique Identifier for string |
| TS | varchar |  |  | SI | Term Status  |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*