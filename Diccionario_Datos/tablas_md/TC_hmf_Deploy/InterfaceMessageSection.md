# TC_hmf_Deploy.InterfaceMessageSection

**Schema:** TC_hmf_Deploy
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Incidentes**. Registro de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HMFDEPSEC_ParRef | varchar | PK |  | NO | Interface Parent Reference |
| HMFDEPSEC_Enabled | bit |  |  | SI | - |
| HMFDEPSEC_SectionDR | varchar |  | FK | SI | - |
| ID | varchar |  |  | NO | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*