# SQLUser.OE_OrdTextResult

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TRES_ParRef | varchar | PK |  | NO | OE_OrdItem Parent Reference |
| ChildQ28DR | - |  |  | SI | Child Reference: Muscle Tone |
| Q27Q1 | - |  |  | SI | Test and Side |
| Q27Q2 | - |  |  | SI | Result |
| Q27Q3 | - |  |  | SI | Comments |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| TRES_Childsub | double |  |  | NO | Childsub |
| TRES_OETR_DR | bigint |  | FK | SI | Des Ref OE TextResult |
| TRES_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*