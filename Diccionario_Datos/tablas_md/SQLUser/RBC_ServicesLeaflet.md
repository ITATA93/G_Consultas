# SQLUser.RBC_ServicesLeaflet

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LFT_ParRef | bigint | PK |  | NO | RBC_Services Parent Reference |
| LFT_Childsub | double |  |  | NO | Childsub |
| LFT_CreatedDate | date |  |  | SI | Created Date |
| LFT_CreatedTime | time |  |  | SI | Created Time |
| LFT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LFT_DateFrom | date |  |  | SI | DateFrom |
| LFT_DateTo | date |  |  | SI | DateTo |
| LFT_Leaflet_DR | bigint |  | FK | SI | Des Ref Leaflet |
| LFT_RowId | varchar |  |  | NO | - |
| LFT_UpdatedDate | date |  |  | SI | Updated Date |
| LFT_UpdatedTime | time |  |  | SI | Updated Time |
| LFT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*