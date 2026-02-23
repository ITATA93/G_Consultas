# websys.MonitorLicenseViewer

> "Class to view the content for Monitor License

**Schema:** websys
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* "Class to view the content for Monitor License

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| LOG_Group_DR | bigint |  | FK | SI | LogonGroup |
| LOG_Hospital_DR | bigint |  | FK | SI | LogonHospital |
| LOG_LOGONID | integer |  |  | SI | Contains the LOGONID as used for SS_UserLogin
det... |
| LOG_Loc_DR | bigint |  | FK | SI | LogonLocation |
| LOG_Profile_DR | bigint |  | FK | SI | LogonProfile |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*