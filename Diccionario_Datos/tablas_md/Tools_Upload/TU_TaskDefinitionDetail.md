# Tools_Upload.TU_TaskDefinitionDetail

**Schema:** Tools_Upload
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TUTDD_ParRef | bigint | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| TUTDD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| TUTDD_CustomProperty | varchar |  |  | SI | Custom Properties - as many as required 
Property... |
| TUTDD_CustomSQL | varchar |  |  | SI | Custom SQL - needs to provide the TaskDefinition s... |
| TUTDD_CustomValue | varchar |  |  | SI | - |
| TUTDD_Description | varchar |  |  | SI | Detailed description  |
| TUTDD_FromDate | date |  |  | SI | - |
| TUTDD_Owner | varchar |  |  | SI | Owner - DEPRECATED - Code Table Overrides |
| TUTDD_PreSelFilterCondition | varchar |  |  | SI | - |
| TUTDD_PreSelFilterOperator | varchar |  |  | SI | AND / OR connection |
| TUTDD_PreSelFilterProperty | varchar |  |  | SI | Filter(s) stored as property ; condition ; value  |
| TUTDD_PreSelFilterSequence | integer |  |  | SI | sequence |
| TUTDD_PreSelFilterValue | varchar |  |  | SI | - |
| TUTDD_ToDate | date |  |  | SI | - |
| TUTDD_UpdDate | date |  |  | SI | - |
| TUTDD_UpdTime | time |  |  | SI | - |
| TUTDD_UpdateProperty | varchar |  |  | SI | Update Properties |
| TUTDD_UpdateValue | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*