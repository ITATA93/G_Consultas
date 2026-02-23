# SQLUser.MRC_DiagnosSignSymptomKeyw

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| KEYW_ParRef | bigint | PK |  | NO | Des Ref to DSYM |
| ChildQ82DR | - |  |  | SI | Child Reference: Sexualidad |
| KEYW_Childsub | numeric |  |  | NO | Childsub |
| KEYW_Desc | varchar |  |  | SI | Description |
| KEYW_Keyword | varchar |  |  | SI | Keyword |
| KEYW_RowId | varchar |  |  | NO | - |
| KEYW_TriageSequence | varchar |  |  | SI | Triage Sequence |
| Q81Q1 | - |  |  | SI | Área |
| Q81Q2 | - |  |  | SI | Evaluación |
| Q81Q3 | - |  |  | SI | Comentarios (Texto libre) |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*