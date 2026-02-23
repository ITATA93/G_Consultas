# SQLUser.RB_PPMSSearch

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PPMS_RowId | bigint | PK |  | NO | - |
| PPMS_Affiliations | varchar |  |  | SI | Affiliations |
| PPMS_DriveTime | double |  |  | SI | Drive Time |
| PPMS_ProviderReason_DR | bigint |  | FK | SI | Provider Preference Reason  |
| PPMS_Reason_DR | bigint |  | FK | SI | Reason for Select |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*