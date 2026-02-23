# SQLUser.OE_OrderLink

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc. Relación entre entidades.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LINK_RowId | bigint | PK |  | NO | - |
| ChildQ36DR | - |  |  | SI | Child Reference: Long Toe |
| LINK_AdmTo_DR | bigint |  | FK | SI | Des Ref PAAdm |
| LINK_CreateDate | date |  |  | SI | CreateDate |
| LINK_CreateTime | time |  |  | SI | CreateTime |
| LINK_CreateUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| LINK_LinkDate | date |  |  | SI | LinkDate |
| LINK_LinkTime | time |  |  | SI | LinkTime |
| LINK_LinkUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| LINK_OrdItemFrom_DR | varchar |  | FK | SI | Des Ref OEOrdItem |
| LINK_OrdItemTo_DR | varchar |  | FK | SI | [DEPRECATED]Deprecated in TrakCare 2016.1+ (Log:TC... |
| LINK_Status | varchar |  |  | SI | Status |
| Q35Q1 | - |  |  | SI | Movement |
| Q35Q2 | - |  |  | SI | Strength - Right |
| Q35Q3 | - |  |  | SI | Strength - Left |
| Q35Q4 | - |  |  | SI | AROM - Right |
| Q35Q5 | - |  |  | SI | AROM - Left |
| Q35Q6 | - |  |  | SI | PROM - Right |
| Q35Q7 | - |  |  | SI | PROM - Left |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*