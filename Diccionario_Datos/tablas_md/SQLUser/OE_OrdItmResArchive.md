# SQLUser.OE_OrdItmResArchive

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OEARC_RowId1 | varchar | PK |  | NO | - |
| ChildQ60DR | - |  |  | SI | Child Reference: Sensory Examination |
| OEARC_ArchiveStatus | varchar |  |  | SI | Archive Status |
| OEARC_CDROMConfirmedDate | date |  |  | SI | Date CDROM Confirmed |
| OEARC_CDROMConfirmedTime | time |  |  | SI | Time CDROM Confirmed |
| OEARC_CDROMCreatedDate | date |  |  | SI | Date CDROM Created |
| OEARC_CDROMCreatedTime | time |  |  | SI | Time CDROM Created |
| OEARC_Comment | varchar |  |  | SI | Comment |
| OEARC_CreatedDate | date |  |  | SI | Date Archive Last Initialised |
| OEARC_CreatedTime | time |  |  | SI | Time Archive Last Initialised |
| OEARC_RowId | varchar |  |  | NO | OE_OrdItmResArchive Row ID |
| OEARC_Size | varchar |  |  | SI | Archive Size(bytes) |
| Q59Q1 | - |  |  | SI | Tendon |
| Q59Q2 | - |  |  | SI | Right |
| Q59Q3 | - |  |  | SI | Left |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*