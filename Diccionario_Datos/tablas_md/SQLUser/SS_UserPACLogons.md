# SQLUser.SS_UserPACLogons

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Registro de eventos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAC_ParRef | bigint | PK |  | NO | SS_User Parent Reference |
| PAC_Childsub | double |  |  | NO | Childsub |
| PAC_LastUpdatedDate | date |  |  | SI | Last Updated Date |
| PAC_LastUpdatedTime | time |  |  | SI | Last Updated Time |
| PAC_LastUpdatedUser | bigint |  |  | SI | Last Updated User |
| PAC_PACSystem | varchar |  |  | SI | PACSystem |
| PAC_Password | varchar |  |  | SI | Password |
| PAC_RowId | varchar |  |  | NO | - |
| PAC_UserName | varchar |  |  | SI | UserName |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*