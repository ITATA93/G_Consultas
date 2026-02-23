# TC_hmf_Generator_Lib_Router_Process_Outbound.Thread1__ChildThreads

**Schema:** TC_hmf_Generator_Lib_Router_Process_Outbound
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Registros hijos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| Thread1 | bigint | PK |  | NO | Parent reference |
| ID | varchar |  |  | NO | - |
| _ChildThreads | varchar |  |  | SI | _ChildThreads |
| element_key | varchar |  |  | NO | %ChildThreads array key |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*