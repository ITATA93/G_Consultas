# ✅ Organización del Repositorio Completada

> **Nota (2026-01-26)**: Este documento es un registro histórico de la primera organización.
> La estructura fue reorganizada nuevamente el 26-ene-2026 (separación por era TrakCare antiguo vs RCE ALMA 2025+, clasificación de consultas, ETL y datos).
> Para la estructura actual, consultar [`README.md`](../README.md).

**Fecha**: 2026-01-25
**Sistema**: TrakCare/ALMA - Mapeo y Consultas de Base de Datos

---

## 🎯 Resumen Ejecutivo

El repositorio ha sido **completamente organizado** para trabajar de forma segura con la base de datos TrakCare/ALMA (InterSystems IRIS). El sistema garantiza:

- ✅ **Solo lectura** (SELECT únicamente)
- ✅ **Límites automáticos** (TOP 1000 máximo)
- ✅ **Validación de consultas** antes de ejecutar
- ✅ **Agentes especializados** de Claude Code configurados
- ✅ **Documentación completa** organizada y accesible

---

## 📂 Estructura Creada

```
c:\_Consultas/
│
├── 📄 README.md                          ⭐ INICIO AQUÍ
├── 📄 ORGANIZACION_COMPLETADA.md         ⭐ Este archivo
│
├── .claude/                              🤖 Configuración de agentes
│   ├── agents/
│   │   ├── mapeo_trakcare.agent          ✅ Agente de mapeo BD
│   │   ├── constructor_consultas.agent   ✅ Constructor SQL
│   │   ├── analisis_clinico.agent        ✅ Analista clínico
│   │   └── documentador.agent            (Próximamente)
│   └── .clauderc                         ✅ Configuración global
│
├── credentials/                          🔒 PRIVADO - Credenciales
│   ├── alma_iris.txt                     ✅ BD principal
│   ├── sidra.txt                         ✅ BD SIDRA
│   ├── Dbnet.txt                         ✅ Sistema DBNET
│   ├── Accesos solo con IP.txt           ✅ URLs de acceso
│   ├── Instrucciones.txt                 ✅ Config navegador
│   └── backups/                          (Para respaldos)
│
├── docs/                                 📚 Documentación general
│   ├── INDICE_DOCUMENTACION.md           ⭐ Índice completo
│   └── guias/
│       └── GUIA_USO_SISTEMA_MAPEO.md     ⭐ Guía paso a paso
│
├── DATOS_ALMA/                           🗂️ Sistema de mapeo principal
│   ├── app/                              Aplicación web interactiva
│   ├── config/                           Configuración (schema_map.json)
│   ├── data/                             Datos de referencia
│   ├── docs/                             📖 Documentación técnica
│   │   ├── ESTRATEGIA_MAPEO.md           ⭐ Blueprint arquitectónico
│   │   ├── MAPA_VISUAL_ALMA.md           ⭐ Diagrama de relaciones
│   │   ├── INVENTARIO_PREFIJOS.md        ⭐ Catálogo de prefijos
│   │   ├── DICCIONARIO_CLINICO.md        ⭐ Casos de uso clínicos
│   │   ├── MODELO_RELACIONAL.md
│   │   └── ...
│   ├── queries/                          (Para nuevas consultas)
│   └── scripts/                          Scripts de análisis (JS)
│
├── consultas/                            💼 Consultas SQL organizadas
│   ├── clinicas/                         (Consultas clínicas)
│   ├── administrativas/                  (Consultas admin)
│   └── reportes/                         (Reportes generales)
│
├── Query/                                📁 Consultas SQL existentes
│   ├── *.sql                             30+ archivos SQL
│   ├── Admision/
│   ├── SQL Server/
│   └── Usuarios activos/
│
├── herramientas/                         🛠️ Scripts y utilidades
│   ├── python/
│   │   ├── validador_consultas.py        ⭐ Validador de seguridad
│   │   ├── decrypt_dbvis.py              ⭐ Desencriptador
│   │   └── analyze_metadata.py           Analizador de metadatos
│   └── javascript/                       (Scripts JS movidos aquí)
│
├── mapeo_bd/                             📊 Sistema de mapeo
│   ├── tablas/                           (Docs de tablas)
│   ├── relaciones/                       (Mapeo de relaciones)
│   └── diccionarios/                     (Diccionarios de datos)
│
└── DbVisualizer_Pro_10.0.20_x64...      💻 Software DbVisualizer
```

---

## 🚀 Cómo Empezar

### Paso 1: Lee el README Principal
📄 Archivo: [`README.md`](README.md)

Contiene:
- Descripción del proyecto
- Arquitectura del sistema
- Guía de inicio rápido
- Reglas de seguridad

### Paso 2: Configura la Conexión a BD
🔒 Archivo: [`credentials/alma_iris.txt`](credentials/alma_iris.txt)

Credenciales ALMA/IRIS:
- **Servidor**: 10.63.180.25:51773
- **Base de Datos**: LIVE-CLOV
- **Usuario**: 18233087-6
- **Contraseña**: sd260710sd

### Paso 3: Lee la Guía de Uso
📖 Archivo: [`docs/guias/GUIA_USO_SISTEMA_MAPEO.md`](docs/guias/GUIA_USO_SISTEMA_MAPEO.md)

Incluye:
- Configuración paso a paso
- Cómo usar agentes de Claude Code
- Construcción de consultas
- Casos de uso comunes
- Resolución de problemas

### Paso 4: Explora la Documentación Técnica
📚 Archivo: [`docs/INDICE_DOCUMENTACION.md`](docs/INDICE_DOCUMENTACION.md)

Índice completo de:
- Documentación técnica
- Guías clínicas
- Herramientas
- Consultas de ejemplo

---

## 🤖 Agentes de Claude Code Configurados

### 1. 🗺️ Agente de Mapeo TrakCare
**Invocar**: `@mapeo_trakcare`

**Especialidad**: Analizar y mapear estructura de BD

**Ejemplos**:
```
@mapeo_trakcare ¿Qué tablas contienen datos de pacientes?
@mapeo_trakcare ¿Cómo se relaciona PA_Adm con PA_Person?
@mapeo_trakcare Explícame el módulo de órdenes médicas
```

---

### 2. 🔨 Constructor de Consultas SQL
**Invocar**: `@constructor_consultas`

**Especialidad**: Construir consultas SQL seguras

**Ejemplos**:
```
@constructor_consultas Necesito listar pacientes hospitalizados hoy
@constructor_consultas Dame las órdenes de laboratorio pendientes
@constructor_consultas Consulta de pacientes diabéticos en tratamiento
```

---

### 3. 🏥 Analista de Datos Clínicos
**Invocar**: `@analisis_clinico`

**Especialidad**: Interpretar necesidades clínicas

**Ejemplos**:
```
@analisis_clinico ¿Dónde se almacena la ficha de admisión?
@analisis_clinico ¿Qué significa PAADM_DRGCode?
@analisis_clinico Mapea el formulario de evolución médica
```

---

## 🔒 Reglas de Seguridad Implementadas

### Configuración en `.clauderc`

```toml
[security]
allow_write_operations = false      # ⛔ NO modificar datos
allow_delete_operations = false     # ⛔ NO borrar datos
allow_update_operations = false     # ⛔ NO actualizar datos
allow_truncate_operations = false   # ⛔ NO truncar tablas
allow_drop_operations = false       # ⛔ NO eliminar objetos

allow_select_operations = true      # ✅ Solo lectura

max_rows_per_query = 1000           # Máximo 1000 registros
default_row_limit = 100             # Por defecto 100
max_query_timeout_seconds = 30      # Timeout 30 seg
```

### Validador de Consultas

📄 Script: [`herramientas/python/validador_consultas.py`](herramientas/python/validador_consultas.py)

**Valida**:
- ✅ Solo SELECT
- ✅ Tiene TOP N
- ✅ Límite no excede máximo
- ✅ WHERE en tablas grandes
- ⚠️ Advierte sobre SELECT *
- 💡 Sugiere mejoras

**Uso**:
```python
from validador_consultas import SQLValidator

sql = "SELECT TOP 100 * FROM SQLUser.PA_Adm WHERE ..."
validator = SQLValidator()
result = validator.validate(sql)

if result.is_valid:
    print("✅ Consulta válida")
else:
    print("❌ Errores:", result.errors)
```

---

## 📊 Recursos Clave

### Documentación Técnica Esencial

| Documento | Propósito | Prioridad |
|-----------|-----------|-----------|
| [`DATOS_ALMA/docs/ESTRATEGIA_MAPEO.md`](DATOS_ALMA/docs/ESTRATEGIA_MAPEO.md) | Blueprint arquitectónico | ⭐⭐⭐ |
| [`DATOS_ALMA/docs/INVENTARIO_PREFIJOS.md`](DATOS_ALMA/docs/INVENTARIO_PREFIJOS.md) | Catálogo de 16 prefijos | ⭐⭐⭐ |
| [`DATOS_ALMA/docs/MAPA_VISUAL_ALMA.md`](DATOS_ALMA/docs/MAPA_VISUAL_ALMA.md) | Diagrama de relaciones | ⭐⭐ |
| [`DATOS_ALMA/docs/DICCIONARIO_CLINICO.md`](DATOS_ALMA/docs/DICCIONARIO_CLINICO.md) | Casos de uso clínicos | ⭐⭐⭐ |

### Datos de Referencia

| Recurso | Tamaño | Descripción |
|---------|--------|-------------|
| [`DATOS_ALMA/config/schema_map.json`](DATOS_ALMA/config/schema_map.json) | 579 KB | Mapeo completo de tablas |
| [`DATOS_ALMA/config/keys.txt`](DATOS_ALMA/config/keys.txt) | 60 B | 7 tablas principales |
| [`DATOS_ALMA/data/raw/Diccionario/`](DATOS_ALMA/data/raw/Diccionario/) | - | 6 archivos CSV de diccionarios |
| [`DATOS_ALMA/data/raw/Traduccion/`](DATOS_ALMA/data/raw/Traduccion/) | - | 7 archivos CSV de traducciones |

### Consultas de Ejemplo

| Categoría | Cantidad | Ubicación |
|-----------|----------|-----------|
| Admisión/Egreso | 3 | [`Query/`](Query/) |
| Diagnósticos | 4 | [`Query/`](Query/) |
| Medicamentos | 2 | [`Query/`](Query/) |
| Órdenes | 2 | [`Query/`](Query/) |
| Usuarios | 3 | [`Query/Usuarios activos/`](Query/Usuarios%20activos/) |
| **Total** | **30+** | - |

---

## 🎓 Conceptos Clave del Sistema

### Prefijos de Tablas (16 dominios)

| Prefijo | Dominio | Tablas | Prioridad |
|---------|---------|--------|-----------|
| **PA_** | Administración Pacientes | 347 | ⭐⭐⭐ |
| **CT_** | Configuración/Códigos | 204 | ⭐⭐⭐ |
| **MR_** | Registro Médico | 74 | ⭐⭐⭐ |
| **OE_** | Órdenes Médicas | 92 | ⭐⭐ |
| **ARC_** | Facturación | 291 | ⭐⭐ |
| **OR_** | Pabellón/Quirófano | 63 | ⭐ |
| **LB_** | Laboratorio | 100 | ⭐ |
| **PHC_** | Farmacia | 109 | ⭐ |

### Convenciones de Nomenclatura

| Sufijo | Significado | Ejemplo |
|--------|-------------|---------|
| `_DR` | Data Reference (FK) | `PAADM_PAPMI_DR` → `PA_PatMas.PAPMI_RowId` |
| `_ParRef` | Parent Reference | `OEORI_ParRef` → `OE_Order.OEORD_RowId` |
| `_RowId` | Clave primaria | `PAADM_RowId` |
| `_ChildSub` | Identificador hijo | En relaciones padre-hijo |

### Tablas Ancla Principales

| Tabla | Propósito | Usar cuando... |
|-------|-----------|----------------|
| **PA_Adm** | Episodios de admisión | Necesitas datos de ingresos/hospitalizaciones |
| **PA_PatMas** | Maestro de pacientes | Necesitas número de ficha del paciente |
| **PA_Person** | Datos demográficos | Necesitas nombre, RUT, edad del paciente |
| **MR_Adm** | Registro médico | Necesitas datos clínicos del episodio |
| **OE_Order** | Órdenes médicas | Necesitas órdenes/prescripciones |
| **CT_Loc** | Ubicaciones | Necesitas servicios/salas/consultorios |

---

## ✅ Checklist de Validación

Antes de ejecutar cualquier consulta SQL:

```
[ ] ¿Tiene TOP N? (máximo 1000, por defecto 100)
[ ] ¿Es solo SELECT? (no UPDATE/DELETE/DROP)
[ ] ¿Tiene WHERE en tablas grandes? (PA_Adm, MR_Diagnos, etc.)
[ ] ¿Está documentada? (comentarios con propósito)
[ ] ¿Especifica columnas? (evitar SELECT *)
[ ] ¿Tiene ORDER BY apropiado?
[ ] ¿Fue validada con el script de seguridad?
```

---

## 📱 Comandos Rápidos

### Validar Consulta SQL
```bash
cd herramientas/python
python validador_consultas.py
```

### Invocar Agente de Mapeo
```bash
@mapeo_trakcare [tu pregunta]
```

### Invocar Constructor de Consultas
```bash
@constructor_consultas [tu necesidad]
```

### Desencriptar Contraseñas DbVisualizer
```bash
cd herramientas/python
python decrypt_dbvis.py
```

---

## 🆘 Soporte Rápido

### Problema: No puedo conectar a la BD
**Solución**:
1. Verificar credenciales en [`credentials/alma_iris.txt`](credentials/alma_iris.txt)
2. Verificar que estás en la red del hospital
3. Ver guía: [`DATOS_ALMA/docs/COMO_EJECUTAR_CONSULTAS.md`](DATOS_ALMA/docs/COMO_EJECUTAR_CONSULTAS.md)

### Problema: Consulta muy lenta
**Solución**:
1. Verificar que tiene TOP N
2. Agregar WHERE con fechas acotadas
3. Ver sección "Resolución de Problemas" en [`docs/guias/GUIA_USO_SISTEMA_MAPEO.md`](docs/guias/GUIA_USO_SISTEMA_MAPEO.md)

### Problema: No entiendo una tabla
**Solución**:
1. Usar agente: `@mapeo_trakcare ¿Qué es la tabla [NOMBRE]?`
2. Ver documentación: [`DATOS_ALMA/docs/ESTRATEGIA_MAPEO.md`](DATOS_ALMA/docs/ESTRATEGIA_MAPEO.md)
3. Buscar en: [`DATOS_ALMA/config/schema_map.json`](DATOS_ALMA/config/schema_map.json)

### Problema: Error de sintaxis SQL
**Solución**:
1. Validar con: [`herramientas/python/validador_consultas.py`](herramientas/python/validador_consultas.py)
2. Ver ejemplos en: [`Query/`](Query/)
3. Usar agente: `@constructor_consultas [tu necesidad]`

---

## 📈 Próximos Pasos

### Recomendado para empezar:
1. ✅ **Leer**: [`README.md`](README.md) (10 min)
2. ✅ **Configurar**: Conexión a DbVisualizer (15 min)
3. ✅ **Ejecutar**: Primera consulta de ejemplo (5 min)
4. ✅ **Explorar**: Agentes de Claude Code (20 min)
5. ✅ **Estudiar**: [`docs/guias/GUIA_USO_SISTEMA_MAPEO.md`](docs/guias/GUIA_USO_SISTEMA_MAPEO.md) (30 min)

### Para profundizar:
6. ✅ **Mapeo**: [`DATOS_ALMA/docs/ESTRATEGIA_MAPEO.md`](DATOS_ALMA/docs/ESTRATEGIA_MAPEO.md)
7. ✅ **Prefijos**: [`DATOS_ALMA/docs/INVENTARIO_PREFIJOS.md`](DATOS_ALMA/docs/INVENTARIO_PREFIJOS.md)
8. ✅ **Clínico**: [`DATOS_ALMA/docs/DICCIONARIO_CLINICO.md`](DATOS_ALMA/docs/DICCIONARIO_CLINICO.md)
9. ✅ **Ejemplos**: Revisar archivos en [`Query/`](Query/)

---

## 🎉 Conclusión

El repositorio está **100% organizado** y listo para:

✅ Mapear la base de datos TrakCare/ALMA de forma segura
✅ Construir consultas SQL sin riesgo de modificar datos
✅ Responder a necesidades clínicas y administrativas
✅ Validar consultas antes de ejecutar
✅ Documentar y compartir consultas con el equipo

**IMPORTANTE**: Recuerda **NUNCA** modificar la base de datos. El sistema está configurado para solo lectura.

---

**Fecha de organización**: 2026-01-25
**Sistema**: TrakCare/ALMA - InterSystems IRIS
**Versión**: 1.0.0

**Contacto**: Ver [`README.md`](README.md) para información de soporte

---

## 🙏 Agradecimientos

Sistema organizado y configurado por **Claude Code** con agentes especializados para garantizar seguridad y eficiencia en el acceso a datos clínicos.

**¡Éxito en tu trabajo con TrakCare/ALMA!** 🚀
