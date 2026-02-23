# SQLUser.IKDocumentSentencePart

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| Sentence | varchar | PK |  | NO | - |
| CRCMaster | integer |  |  | SI | - |
| CRCSlave | integer |  |  | SI | - |
| EntityUniqueId | varchar |  |  | SI | - |
| HighLevelConcept | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| IndexValue | varchar |  |  | SI | - |
| PartType | varchar |  |  | SI | - |
| Value | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| isNegation | bit |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*