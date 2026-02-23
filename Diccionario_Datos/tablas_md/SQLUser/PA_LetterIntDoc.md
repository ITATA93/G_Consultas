# SQLUser.PA_LetterIntDoc

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INTDOC_ParRef | bigint | PK |  | NO | PA_Letter Parent Reference |
| INTDOC_Childsub | double |  |  | NO | Childsub |
| INTDOC_IntDoc_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| INTDOC_RowId | varchar |  |  | NO | - |
| Q03Q1 | - |  |  | SI | Substance trialled |
| Q03Q10 | - |  |  | SI | Oesophageal stage |
| Q03Q2 | - |  |  | SI | Administration method |
| Q03Q3 | - |  |  | SI | Response |
| Q03Q4 | - |  |  | SI | Response comments |
| Q03Q5 | - |  |  | SI | Strategies / Manoeuvres |
| Q03Q6 | - |  |  | SI | Strategies / Manoeuvres comments and response |
| Q03Q7 | - |  |  | SI | Pre oral stage |
| Q03Q8 | - |  |  | SI | Oral stage |
| Q03Q9 | - |  |  | SI | Pharyngeal stage |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*