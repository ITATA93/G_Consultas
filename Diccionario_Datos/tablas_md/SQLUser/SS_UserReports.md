# SQLUser.SS_UserReports

**Schema:** SQLUser
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| USREP_ParRef | bigint | PK |  | NO | SS_User Parent Reference |
| USREP_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| USREP_Childsub | double |  |  | NO | Childsub |
| USREP_Device_DR | varchar |  | FK | SI | Des Ref Device |
| USREP_Report_DR | bigint |  | FK | SI | Des Ref Report(Module Report) |
| USREP_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*