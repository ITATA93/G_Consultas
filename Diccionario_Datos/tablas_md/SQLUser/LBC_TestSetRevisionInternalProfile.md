# SQLUser.LBC_TestSetRevisionInternalProfile

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCTSRIP_ParRef | bigint | PK |  | NO | Parent Revision |
| ChildQ05DR | - |  |  | SI | Child Reference: Definición de Problemas a Interve... |
| LBCTSRIPI_DisableAuth | varchar |  |  | SI | Disable Authorisation |
| LBCTSRIP_DateFrom | date |  |  | SI | Start date the record is active |
| LBCTSRIP_DateTo | date |  |  | SI | Last date the record is active  |
| LBCTSRIP_Queue_DR | bigint |  | FK | SI | Queue |
| LBCTSRIP_RowID | varchar |  |  | NO | - |
| Q04Q1 | - |  |  | SI | Acciones |
| Q04Q2 | - |  |  | SI | Responsables |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*