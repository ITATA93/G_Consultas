# lab.CT_ServiceKPIDetails

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTKPID_ParRef | varchar | PK |  | NO | CT_ServiceLevelKPI Parent Reference |
| CTKPID_KPIType | varchar |  |  | SI | KPI Type |
| CTKPID_Percentage | integer |  |  | SI | Percentage |
| CTKPID_RowID | varchar |  |  | NO | - |
| CTKPID_Sequence | varchar |  |  | NO | Sequence |
| CTKPID_UserGroup_DR | bigint |  | FK | SI | Contact User Group DR |
| CTKPID_User_DR | varchar |  | FK | SI | Contact User DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*