# SQLUser.SS_Device

**Schema:** SQLUser
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SS_Device1 | varchar | PK |  | NO | - |
| DEV_Name | varchar |  |  | SI | General Name |
| DEV_SystemName | varchar |  |  | SI | System Name |
| DEV_TermType_DR | varchar |  | FK | SI | Des Ref TermType |
| DEV_Type | varchar |  |  | SI | Type |
| SS_Device | varchar |  |  | NO | Device Name |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*