# SQLUser.OE_OrdItmResArchiveFile

**Schema:** SQLUser
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OEARF_ParRef | varchar | PK |  | NO | OE_OrdItmResArchive Parent Reference |
| ChildQ61DR | - |  |  | SI | Child Reference: Movement Loss / Muscle Power |
| OEARF_FileName | varchar |  |  | NO | File Name |
| OEARF_OEOrdResult_DR | varchar |  | FK | SI | Des Ref OE OrdResult |
| OEARF_RowId | varchar |  |  | NO | - |
| Q60Q1 | - |  |  | SI | Location |
| Q60Q2 | - |  |  | SI | Sensation |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*